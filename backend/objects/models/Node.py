from django.db import models
from app.Enums.ModelEnums import CalculationMode, ObjectType
from flowsheet.models import WeatherData
from objects.models.NodeFactory import NodeFactory
from objects.models.PropertyModels import Formula, PropertyInfo, PropertySet
from flowsheet.models import Project
import sympy as sp

factory = NodeFactory()

class Node(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_nodes")
    position = models.ForeignKey("NodePosition", on_delete=models.CASCADE, related_name="position_node")
    type = models.CharField(choices=ObjectType, default=ObjectType.SolarPanel)
    calculation_mode = models.CharField(choices=CalculationMode.choices, default=CalculationMode.SolarPowerBased)

    @classmethod
    def create(cls, project, type, x=0, y=0):
        """
        Create a Node with associated properties and property sets based on the configuration.
        """
        print('here')
        wi = WeatherData.create(lat=-37.719408, lon=175.248599)
        print(wi)

        # Get configuration for the Node type
        config = factory.get_configuration(object_type=type)
        property_sets_config = config.pop("propertySets")

        # Create the Node instance
        position = NodePosition.objects.create(x=x, y=y)
        position.save()

        node = Node.objects.create(project=project, position=position, type=type, **config)
        node.save()

        # Create Property Sets and Properties
        for property_set_config in property_sets_config:
            formulas = property_set_config.pop("formulas", [])

            property_set = PropertySet.objects.create(name=property_set_config["name"], node=node)

            for formula in formulas:
                Formula.objects.create(property_set=property_set, **formula)

            property_set.save()
            create_properties(property_set_config["properties"], property_set)

        return node

    def get_property_set(self, set_name="Default") -> PropertySet:
        """
        Returns a contained property set by name
        """
        return self.property_sets.filter(name=set_name).first()

    def calculate_outputs(self) -> None:
        """
        Automatically calculate outputs based on property metadata and formulas.
        """
        calc_set = self.get_property_set(self.calculation_mode)
        output_set = self.get_property_set("Outputs")

        if not calc_set:
            raise ValueError(f"No property set found for mode {self.calculation_mode}")

        formulas = calc_set.get_formulas()  # Retrieve all formulas for the property set
        if not formulas.exists():
            raise ValueError(f"No formulas found for property set {calc_set.name}")

        input_values = {}
        for prop in calc_set.properties.all():
            if prop.defined and prop.value is not None:
                input_values[prop.key] = float(prop.value)
            else:
                return

        try:
            # Evaluate each formula
            for formula in formulas:
                formula_expr = sp.sympify(formula.formula_expression)
                variables = {sp.Symbol(k): v for k, v in input_values.items()}
                result = float(formula_expr.evalf(subs=variables))

                # Save the result to the appropriate output property
                if output_set:
                    output_prop = output_set.get_property(formula.output_property)
                    if output_prop:
                        output_prop.value = round(result, 3)
                        output_prop.defined = True
                        output_prop.save()

                        input_values[formula.output_property] = result

            # Refetch outputs as inputs
            output_formulas = output_set.get_formulas()
            for prop in output_set.properties.all():
                if prop.value is not None:
                    input_values[prop.key] = prop.value
                else:
                    return

            for formula in output_formulas:
                formula_expr = sp.sympify(formula.formula_expression)
                variables = {sp.Symbol(k): v for k, v in input_values.items()}
                result = float(formula_expr.evalf(subs=variables))

                # Save the result to the corresponding output property
                output_prop = output_set.get_property(formula.output_property)
                if output_prop:
                    output_prop.value = round(result, 3)
                    output_prop.defined = True
                    output_prop.save()

        except Exception as e:
            print(f"Error calculating outputs for {self.calculation_mode}: {e}")


class NodePosition(models.Model):
    x = models.FloatField(default=0.0)
    y = models.FloatField(default=0.0)


def create_properties(properties_config, property_set):
    """
    Create and associate properties with a PropertySet.
    """
    properties = [
        PropertyInfo(set=property_set, **property_config)
        for property_config in properties_config
    ]
    PropertyInfo.objects.bulk_create(properties)

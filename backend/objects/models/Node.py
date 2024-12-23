from django.db import models
from app.Enums.ModelEnums import CalculationMode, ObjectType
from objects.models.PropertyModels import PropertyInfo, PropertySet
from objects.models.Configs import get_object_configuration
from flowsheet.models import Project
import sympy as sp

class Node(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_nodes')
    position = models.ForeignKey("NodePosition", on_delete=models.CASCADE, related_name="position_node")
    type = models.CharField(choices=ObjectType, default=ObjectType.SolarPanel)
    calculation_mode = models.CharField(choices=CalculationMode.choices, default=CalculationMode.SolarPowerBased)

    @classmethod
    def create(cls, project, type, x=0, y=0):
        """
        Create a Node with associated properties and property sets based on the configuration.
        """
        # Get configuration for the Node type
        config = get_object_configuration(type=type)
        property_sets_config = config.pop('propertySets')  # Retrieve property sets configuration

        # Create the Node instance
        position = NodePosition.objects.create(x=x, y=y)
        position.save()

        node = Node.objects.create(
            project=project,
            position=position,
            type=type,
            **config
        )
        node.save()

        # Create Property Sets and Properties
        for property_set_config in property_sets_config:
            property_set = PropertySet.objects.create(
                name=property_set_config['name'],
                formula=property_set_config.get('formula', None),
                node=node
            )
            property_set.save()
            create_properties(property_set_config['properties'], property_set)
            
        return node

    def get_property_set(self, set_name="Default") -> PropertySet:
        return self.property_sets.filter(name=set_name).first()
    
    def calculate_outputs(self):
        """
        Automatically calculate outputs based on property metadata and formulas.
        """
        calc_set = self.get_property_set(self.calculation_mode)
        input_values = {}

        if not calc_set or not calc_set.formula:
            print(f"No formula or property set found for mode {self.calculation_mode}")
            return
        
        for prop in calc_set.properties.all():
            if prop.defined and prop.value is not None:
                input_values[prop.key] = prop.value
            else:
                return

        try:
            formula = sp.sympify(calc_set.formula)
            variables = {sp.Symbol(k): v for k, v in input_values.items()}
            result = float(formula.evalf(subs=variables))

            # Save the result to the "Outputs" property set
            output_set = self.get_property_set("Outputs")
            if output_set:
                output_prop = output_set.get_property("daily_energy")
                if output_prop:
                    output_prop.value = result
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

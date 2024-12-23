# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from objects.models.PropertyModels import PropertyInfo

# @receiver(post_save, sender=PropertyInfo)
# def trigger_node_calculation(sender, instance, **kwargs):
#     """
#     Trigger node calculation when a PropertyInfo is updated.
#     """
#     # Access the PropertySet and its associated Node
#     property_set = instance.set
#     node = property_set.node

#     # Only trigger if the updated property is an input and has a valid value
#     if instance.defined and instance.value is not None and node:
#         post_save.disconnect(trigger_node_calculation, sender=sender)
#         node.calculate_outputs()
#         post_save.connect(trigger_node_calculation, sender=sender)


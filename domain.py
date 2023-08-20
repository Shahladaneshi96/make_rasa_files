intent_list=['greeting','search','phone_question','out_of_scope','reset','change','sort','decrease_price','increase_price']
entity_list=['price_SetValueOp','price_ClearValueOp','price_ClearFacetOp','price_lower_SetValueOp','price_lower_ClearValueOp','price_lower_ClearFacetOp','price_upper_SetValueOp','price_upper_ClearValueOp','price_upper_ClearFacetOp','ram_SetValueOp','ram_ClearValueOp','ram_ClearFacetOp','ram_lower_SetValueOp','ram_lower_ClearValueOp','ram_lower_ClearFacetOp','ram_upper_SetValueOp','ram_upper_ClearValueOp','ram_upper_ClearFacetOp','mem_SetValueOp','mem_ClearValueOp','mem_ClearFacetOp','mem_lower_SetValueOp','mem_lower_ClearValueOp','mem_lower_ClearFacetOp','mem_upper_SetValueOp','mem_upper_ClearValueOp','mem_upper_ClearFacetOp','slot_type_SetValueOp','slot_type_ClearValueOp','slot_type_ClearFacetOp','brand_SetValueOp','brand_ClearValueOp','color_SetValueOp','color_ClearValueOp','resolution_upper_SetValueOp','resolution_lower_SetValueOp','resolution_SetValueOp','sim_count_SetValueOp','slot_type_sort','slot_type_sort_ascending','slot_type_sort_descending','slot_type_change_decrease','slot_type_change_increase','slot_type_change_categorical','brand_ClearFacetOp','camera_ClearFacetOp','camera_lower_ClearValueOp','camera_upper_ClearValueOp','sim_count_ClearFacetOp']
slot_list=['price_SetValueOp','price_ClearValueOp','price_ClearFacetOp','price_lower_SetValueOp','price_lower_ClearValueOp','price_lower_ClearFacetOp','price_upper_SetValueOp','price_upper_ClearValueOp','price_upper_ClearFacetOp','ram_SetValueOp','ram_ClearValueOp','ram_ClearFacetOp','ram_lower_SetValueOp','ram_lower_ClearValueOp','ram_lower_ClearFacetOp','ram_upper_SetValueOp','ram_upper_ClearValueOp','ram_upper_ClearFacetOp','mem_SetValueOp','mem_ClearValueOp','mem_ClearFacetOp','mem_lower_SetValueOp','mem_lower_ClearValueOp','mem_lower_ClearFacetOp','mem_upper_SetValueOp','mem_upper_ClearValueOp','mem_upper_ClearFacetOp','slot_type_SetValueOp','slot_type_ClearValueOp','slot_type_ClearFacetOp','brand_SetValueOp','brand_ClearValueOp','color_SetValueOp','color_ClearValueOp','resolution_upper_SetValueOp','resolution_lower_SetValueOp','resolution_SetValueOp','sim_count_SetValueOp','slot_type_sort','slot_type_sort_ascending','slot_type_sort_descending','slot_type_change_decrease','slot_type_change_increase','slot_type_change_categorical','brand_ClearFacetOp','camera_ClearFacetOp','camera_lower_ClearValueOp','camera_upper_ClearValueOp','sim_count_ClearFacetOp']
intent_slot_list=['search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search','search']


intent_json_file = open("/content/domain.yml", "a")

header1 = 'version: "3.1"'+'\n\n'+'intents:'

intent_json_file.write(header1)

for intent in intent_list:
  header2 = '\n'+'  - ' +intent
  intent_json_file.write(header2)

header3 = '\n\n'+'entities:'+'\n'
intent_json_file.write(header3)

for entity in entity_list:
  header4 = '\n'+'  - ' +entity
  intent_json_file.write(header4)

header5 = '\n\n'+'slots:'+'\n'
intent_json_file.write(header5)

for slot,intent in zip(slot_list,intent_slot_list):
  header6 = '\n  '+slot+':\n    '+'type: text'+':\n    '+'initial_value: not_set'+':\n    '+'mappings:'+':\n    '+'- type: from_entity'+'\n      '+'entity: '+slot+'\n      '+'intent:'+'\n      - '+intent+'\n'
  intent_json_file.write(header6)

intent_json_file.close()
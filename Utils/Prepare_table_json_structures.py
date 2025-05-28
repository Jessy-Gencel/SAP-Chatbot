from DB.Hanaconnection import connection, inspector
import json

def prepare_table_json_structures() -> dict:
    """
    Retrieve metadata for all views in the specified SAP HANA schema and return it as a JSON-formatted string.

    This function connects to the 'DBE_00_INNOVATION' schema, retrieves all view names,
    extracts their column metadata (name and type), and constructs a dictionary
    where each view name maps to its list of column definitions.

    Returns:
        str: A JSON-formatted string containing the metadata of all views and their columns.
    """

    dbConsumptionSchema = 'DBE_00_INNOVATION'
    views = inspector.get_view_names(schema=dbConsumptionSchema.lower())
    all_metadata = []
    for view in views:
        columns = inspector.get_columns(table_name=view, schema=dbConsumptionSchema.lower())
        all_metadata.append((view,columns))
    
    metadata_dict = {}
    for view, columns in all_metadata:
        metadata_dict[view] = {
            'columns' : [{'name': col['name'],'type': str(col['type'])} for col in columns]
        }
    all_metadata_json = json.dumps(metadata_dict, indent=4)
    return all_metadata,all_metadata_json

all_metadata, metadata_json = prepare_table_json_structures()
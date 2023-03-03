def query_get_matter_and_submatter_by_user(user_id):
    """
    Return a SQL query string that selects information about matters and their submatters for a specified user_id.

    Args:
        user_id (int): The ID of the user for whom
        the information is being queried.

    Returns:
        str: A SQL query string.
            The query selects the following columns:
                - `mt.id`: the ID of the primary matter
                - `mt.name`: the name of the primary matter
                - `fm.required`: a field from the `formule` table
                - `mt2.id`: the ID of the secondary matter (i.e.,
                the submatter)
                - `mt2.name`: the name of the secondary matter
                - `mt.user_id`: the ID of the user to whom the matters belong
            The query joins three tables: `matter`, `formule`, and `matter`
            (again, but with an alias of `mt2`).
            The `join` clauses connect the tables
            based on their primary and foreign keys.
    """
    return f'''
        SELECT
        mt.id, mt.name,fm.required,
        mt2.id as secondary_id , mt2.name as secondary_name,
        mt.user_id
        FROM matter mt 
        join formule fm on mt.id = fm.id_primary
        join matter mt2 on mt2.id = fm.id_secondary
        where mt.user_id = {user_id}'''

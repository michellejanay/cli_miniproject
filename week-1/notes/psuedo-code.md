# add some product names
CREATE products list

PRINT main menu options
GET user input for main menu option

IF user input is 0:
    EXIT app

# products menu
ELSE IF user input is 1:

    PRINT product menu options
    GET user input for product menu option

    IF user input is 0:
        RETURN to main menu

    ELSE IF user input is 1:
        PRINT products list

    ELSE IF user input is 2:

        # CREATE new product
        GET user input for product name
        APPEND product name to products list

    ELSE IF user input is 3:
    
        # STRETCH GOAL - UPDATE existing product
        PRINT product names with its index value
        GET user input for product index value
        GET user input for new product name
        UPDATE product name at index in products list

    ELSE IF user input is 4:

        # STRETCH GOAL - DELETE product
        PRINT products list
        GET user input for product index value
        DELETE product at index in products list

def dividing_line():
    """ This is a dividing line for formating in my final report"""
    print "*" * 80

def calculate_orders_by_type(file_path):
    """Calculates the orders by type.

    Given a text file in the format:
    19|Watermelon|54
    sales person id|melon type|melon count

    This function will total the melons by type and display the totals
    """
    #open the data file
    my_file = open("orders-by-type.txt")

    #define variable
    melon_tallies = {"Musk": 0, "Hybrid": 0, "Watermelon": 0, "Winter": 0}

    #iterate through file data and calculate the count by melon type
    for line in my_file:
        data = line.split("|")
        melon_type = data[1]
        melon_count = int(data[2])
        melon_tallies[melon_type] += melon_count

    my_file.close()

    #print dividing line
    dividing_line()

    #define variables
    melon_prices = {"Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00}
    total_revenue = 0

    #iterate through data and calculate sales totals
    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue

        #print the totals
        print "We sold {} {} melons at {:.2f} each for a total of {:.2f}".format(melon_tallies[melon_type], melon_type, price, revenue)

    #print dividing line
    dividing_line()


def calculate_sales_by_sale_type(file_path):
    """Calculates the sales by sale type.

    Given data in a file in the format:
    4|0|ONLINE|72.17
    5|57|Janice West|104.94
    ID|some number|some name|sale amount

    This function will calculate the Online and Salesperson sales
    and display the totals
    """

    #open data file
    my_file = open(file_path)

    #define variable
    sales = [0, 0]

    #iterate through file data and calculate sales totals
    for line in my_file:
        d = line.split("|")
        if d[1] == "0":
            sales[0] += float(d[3])
        else:
            sales[1] += float(d[3])

    #print dividing line
    dividing_line()

    print "Salespeople generated ${:.2f} in revenue.".format(sales[1])
    print "Internet sales generated ${:.2f} in revenue.".format(sales[0])
    if sales[1] > sales[0]:
        print "Guess there's some value to those salespeople after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"

    my_file.close()

    #print dividing line
    dividing_line()

#call function to calculate and display orders by melon_type
calculate_orders_by_type("orders-by-type.txt")
calculate_sales_by_sale_type("orders-with-sales.txt")

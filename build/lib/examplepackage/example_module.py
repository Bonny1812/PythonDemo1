def example_function(spark):
    print("Hello World! I bet you didn't expect that.")
    customer = [(1,"Smith",4343,"GOOG",'2022-04-27 09:15:00',250,"insert"), \
    (2,"Rose",1333,"MSFT",'2022-04-27 09:15:00',225,"update"), \
    (3,None,13434,None,'2022-04-27 09:15:00',150,"insert"), \
    (4,"Jones",2343,"APPL",'2022-04-27 09:15:00',200,None)  ]
    customerColumns = ["cid","name","sellerid","company","order_date","amount","flag"]
    cDF = spark.createDataFrame(data=customer, schema = customerColumns)
    cDF.show()
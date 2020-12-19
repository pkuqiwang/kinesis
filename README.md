# How to use Python Kinesiis agent to Push meesages into Kinesis Data stream
 
this is a code sample of how to use Python to push large numebr of code into Kinesis data test in the readme

Use the following code in AWS CLI to create the Kinesis data stream for the sample
```aws kinesis create-stream --stream-name ExampleInputStream --shard-count 1```

then use `PutRecond_Kinesis.py` to send the messages to the Kinesis data stream you just created.



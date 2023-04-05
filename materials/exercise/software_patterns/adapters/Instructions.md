# Exercise 

In this example you have a simple DataScience experiment.
We have a main file that:
    - reads the config 
    - creates an experiment instance 
    - runs the experiment 

The config (JSON) itself contains typical values for the experiment definition. 
The Experiment:
    - loads data 
    - sets up in environment 
    - run the experiment 

Everything works fine. 
Now you are ask to also support xml configs since it a common format and your colleagues want to use your code with it. 
How do you do that using the Adapter pattern? 

An example config may look like this:
```xml
<config>
    <epoch_count>40</epoch_count>
    <lr>5e-5</lr>
    <batch_size>64</batch_size>
    <log_path>./runs</log_path>
    <data_path>./raw_data</data_path>
</config>
```


Hint 1: you can use xml in the standard library 


Hint 2: with the find-method of the xml.etree.ElementTree you can get the first occurrence of a Tag 


Hint 3: If a tag does not exist the ElementTree with throw a NameError 
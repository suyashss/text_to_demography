from pydantic import BaseModel, PositiveFloat, ValidationError
from typing_extensions import Literal
from numpy import random
import numpy as np
import string

popname_arr = list(string.ascii_uppercase) 
changetypes = ['linear','exponential']

increase_desc = ['increased','grew']
decrease_desc = ['decreased','reduced']
change_desc = increase_desc + decrease_desc + ['changed']

change_desc_map = {'increased':'increase', 'grew':'growth','decreased':'decrease',
                       'reduced':'reduction', 'changed':'change'}
change_desc_present = list(change_desc_map.values())


def get_size_change_description(size_from,size_to):
    if random.random() < 0.5:
        return 'changed','change'
    if size_to > size_from:
        desc = increase_desc[random.choice(len(increase_desc))]
    else:
        desc = decrease_desc[random.choice(len(decrease_desc))]
    return desc, change_desc_map[desc]

class Example1(BaseModel):
    pop1: str
    size1: PositiveFloat
    
    @classmethod
    def generate_example(cls):
        high = 10000.0
        low = 100.0
        size1 = random.random(1)*(high-low)+low
        pop1 = random.choice(popname_arr)
        data_dict = {'pop1':pop1,'size1':size1}
        return cls(**data_dict)


class Example2(BaseModel):
    pop1: str
    size1: PositiveFloat
    size2: PositiveFloat
    size1_to_size2_description: Literal[tuple(change_desc)]
    size1_to_size2_description_present: Literal[tuple(change_desc_present)]
    time1: PositiveFloat
    
    @classmethod
    def generate_example(cls):
        size_low, size_high = 100.0, 10000.0
        time_low, time_high = 10.0, 10000.0
        size1, size2 = random.random(2)*(size_high-size_low)+size_low
        time1 = random.random()*(time_high-time_low)+time_low
        pop1 = random.choice(popname_arr)
        size1_to_size2_description, size1_to_size2_description_present = get_size_change_description(size1,size2)
        data_dict = {'pop1':pop1,'size1':size1, 'size2':size2, 'time1': time1, 
                     'size1_to_size2_description': size1_to_size2_description,
                     'size1_to_size2_description_present': size1_to_size2_description_present}
        return cls(**data_dict)

class Example3(BaseModel):
    pop1: str
    size1: PositiveFloat
    size2: PositiveFloat
    size3: PositiveFloat
    size4: PositiveFloat
    size1_to_size2_description: Literal[tuple(change_desc)]
    size1_to_size2_description_present: Literal[tuple(change_desc_present)]
    size2_to_size3_description: Literal[tuple(change_desc)]
    size2_to_size3_description_present: Literal[tuple(change_desc_present)]
    size3_to_size4_description: Literal[tuple(change_desc)]
    size3_to_size4_description_present: Literal[tuple(change_desc_present)]
    time1: PositiveFloat
    time2: PositiveFloat
    time3: PositiveFloat
    changetype1: Literal[tuple(changetypes)]
    changetype2: Literal[tuple(changetypes)]
    changetype3: Literal[tuple(changetypes)]
    
    @classmethod
    def generate_example(cls):
        size_low, size_high = 100.0, 10000.0
        time_low, time_high = 10.0, 10000.0
        size1, size2, size3, size4 = random.random(4)*(size_high-size_low)+size_low
        time1, time2, time3 = [x*(time_high-time_low)+time_low for x in sorted(random.random(3),reverse=True)]
        pop1 = random.choice(popname_arr)
        size1_to_size2_description, size1_to_size2_description_present = get_size_change_description(size1,size2)
        size2_to_size3_description, size2_to_size3_description_present = get_size_change_description(size2,size3)
        size3_to_size4_description, size3_to_size4_description_present = get_size_change_description(size3,size4)
        changetype1, changetype2, changetype3 = [changetypes[x] for x in random.choice(len(changetypes),
                                                                                       size=3)]

        data_dict = {'pop1': pop1,'size1': size1, 'size2': size2, 'size3': size3, 'size4': size4, 
                     'time1': time1, 'time2': time2, 'time3': time3,
                     'size1_to_size2_description': size1_to_size2_description,
                     'size1_to_size2_description_present': size1_to_size2_description_present,
                     'size2_to_size3_description': size2_to_size3_description,
                     'size2_to_size3_description_present': size2_to_size3_description_present,
                     'size3_to_size4_description': size3_to_size4_description,
                     'size3_to_size4_description_present': size3_to_size4_description_present,
                     'changetype1': changetype1, 'changetype2': changetype2,
                     'changetype3': changetype3}

        return cls(**data_dict)
    

class Example4(BaseModel):
    pop1: str
    pop2: str
    pop3: str
    size1: PositiveFloat
    size2: PositiveFloat
    size3: PositiveFloat
    time1: PositiveFloat
    
    @classmethod
    def generate_example(cls):
        size_low, size_high = 100.0, 10000.0
        time_low, time_high = 10.0, 10000.0
        size1, size2, size3 = random.random(3)*(size_high-size_low)+size_low
        time1 = random.random()*(time_high-time_low)+time_low
        pop1, pop2, pop3 = random.choice(popname_arr,3, replace = False)
        data_dict = {'pop1':pop1,'pop2':pop2,'pop3':pop3,
                     'size1':size1, 'size2':size2, 'size3':size3,
                     'time1': time1} 
        return cls(**data_dict)

class Example5(BaseModel):
    pop1: str
    pop2: str
    size1: PositiveFloat
    size2: PositiveFloat
    time1: PositiveFloat
    
    @classmethod
    def generate_example(cls):
        size_low, size_high = 100.0, 10000.0
        time_low, time_high = 10.0, 10000.0
        size1, size2 = random.random(2)*(size_high-size_low)+size_low
        time1 = random.random()*(time_high-time_low)+time_low
        pop1, pop2 = random.choice(popname_arr,2, replace = False)
        data_dict = {'pop1':pop1,'pop2':pop2,
                     'size1':size1, 'size2':size2,
                     'time1': time1} 
        return cls(**data_dict)

class Example6(BaseModel):
    pop1: str
    pop2: str
    pop3: str
    size1: PositiveFloat
    size2: PositiveFloat
    size3: PositiveFloat
    time1: PositiveFloat
    proportion1: PositiveFloat
    proportion2: PositiveFloat
    
    @classmethod
    def generate_example(cls):
        size_low, size_high = 100.0, 10000.0
        time_low, time_high = 10.0, 10000.0
        size1, size2, size3 = random.random(3)*(size_high-size_low)+size_low
        time1 = random.random()*(time_high-time_low)+time_low
        proportion1 = random.random()
        proportion2 = 1 - proportion1
        pop1, pop2, pop3 = random.choice(popname_arr,3, replace = False)
        data_dict = {'pop1':pop1,'pop2':pop2,'pop3':pop3,
                     'proportion1':proportion1,'proportion2':proportion2,
                     'size1':size1, 'size2':size2, 'size3':size3,
                     'time1': time1} 
        return cls(**data_dict)

class Example7(BaseModel):
    pop1: str
    pop2: str
    pop3: str
    size1: PositiveFloat
    size2: PositiveFloat
    size3: PositiveFloat
    time1: PositiveFloat
    time2: PositiveFloat
    time3: PositiveFloat
    time4: PositiveFloat
    time5: PositiveFloat
    rate1: PositiveFloat
    rate2: PositiveFloat
    rate3: PositiveFloat

    @classmethod
    def generate_example(cls):
        size_low, size_high = 100.0, 10000.0
        time_low, time_high = 10.0, 10000.0
        size1, size2, size3 = random.random(3)*(size_high-size_low)+size_low
        time1, time2, time3, time4, time5 = [x*(time_high-time_low)+time_low for x \
                                             in sorted(random.random(5),reverse=True)]
        rate1, rate2, rate3 = random.random(3)
        pop1, pop2, pop3 = random.choice(popname_arr,3, replace = False)
        data_dict = {'pop1':pop1,'pop2':pop2,'pop3':pop3,
                     'rate1':rate1,'rate2':rate2,'rate3':rate3,
                     'size1':size1, 'size2':size2, 'size3':size3,
                     'time1': time1,'time2': time2,'time3': time3,'time4': time4,'time5': time5} 
        return cls(**data_dict)

class Example8(BaseModel):
    pop1: str
    pop2: str
    pop3: str
    size1: PositiveFloat
    size2: PositiveFloat
    size3: PositiveFloat
    time1: PositiveFloat
    rate1: PositiveFloat
    
    @classmethod
    def generate_example(cls):
        size_low, size_high = 100.0, 10000.0
        time_low, time_high = 10.0, 10000.0
        size1, size2, size3 = random.random(3)*(size_high-size_low)+size_low
        time1 = random.random()*(time_high-time_low)+time_low
        rate1 = random.random()
        pop1, pop2, pop3 = random.choice(popname_arr,3, replace = False)
        data_dict = {'pop1':pop1,'pop2':pop2,'pop3':pop3,
                     'rate1':rate1,'time1': time1,
                     'size1':size1, 'size2':size2, 'size3':size3} 
        return cls(**data_dict)

class Example9(BaseModel):
    pop1: str
    pop2: str
    pop3: str
    size1: PositiveFloat
    size2: PositiveFloat
    size3: PositiveFloat
    time1: PositiveFloat
    time2: PositiveFloat
    proportion1: PositiveFloat
    
    @classmethod
    def generate_example(cls):
        size_low, size_high = 100.0, 10000.0
        time_low, time_high = 10.0, 10000.0
        size1, size2, size3 = random.random(3)*(size_high-size_low)+size_low
        time1, time2 = [x*(time_high-time_low)+time_low for x in sorted(random.random(2),reverse=True)]
        proportion1 = random.random()
        pop1, pop2, pop3 = random.choice(popname_arr,3, replace = False)
        data_dict = {'pop1':pop1,'pop2':pop2,'pop3':pop3,
                     'proportion1':proportion1,
                     'size1':size1, 'size2':size2, 'size3':size3,
                     'time1':time1, 'time2':time2} 
        return cls(**data_dict)



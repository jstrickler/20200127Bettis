#!/usr/bin/env python
from dataclasses import dataclass
from datetime import date

@dataclass
class Photo:
    subject: str
    date: date
    
    

if __name__ == '__main__':

    p = Photo('Mom', date(2020,1,1))

    print(p)
    print(p.date)


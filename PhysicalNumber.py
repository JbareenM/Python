#! /usr/bin/env python3
from enum import Enum
class Unit(Enum):
    Km=0
    M=1
    Cm=2
    Hour=3
    Min=4
    Sec=5
    Ton=6
    Kg=7
    G=8
class PhysicalNumber:
    def __init__(self,num,Type):
        self.__num=num
        self.__type=Type
    def __add__(self,other):
        if not self.__checkType(other):
            return None
        val=self.__Diff()*self.__num + other.__Diff()*other.__num
        val/=self.__Diff()
        return PhysicalNumber(val,self.__type)
    def __iadd__(self,other):
        if not self.__checkType(other):
            return None
        val=self.__Diff()*self.__num + other.__Diff()*other.__num
        val/=self.__Diff()
        self.__num=val
        return self
    def __sub__(self,other):
        if not self.__checkType(other):
            return None
        val=self.__Diff()*self.__num - other.__Diff()*other.__num
        val/=self.__Diff()
        return PhysicalNumber(val,self.__type)
    def __isub__(self,other):
        if not self.__checkType(other):
            return None
        val=self.__Diff()*self.__num - other.__Diff()*other.__num
        val/=self.__Diff()
        self.__num=val
        return self
    def __eq__(self,other):
        if not self.__checkType(other):
            return None
        if (self.__Diff()*self.__num)==(other.__Diff()*other.__num):
            return True
        return False
    def __lt__(self,other):
        if not self.__checkType(other):
            return None
        if (self.__Diff()*self.__num)<(other.__Diff()*other.__num):
            return True
        return False
    def __gt__(self,other):
        if not self.__checkType(other):
            return None
        if (self.__Diff()*self.__num)>(other.__Diff()*other.__num):
            return True
        return False
    def __le__(self,other):
        if not self.__checkType(other):
            return None
        if (self.__Diff()*self.__num)<=(other.__Diff()*other.__num):
            return True
        return False
    def __ge__(self,other):
        if not self.__checkType(other):
            return None
        if (self.__Diff()*self.__num)>=(other.__Diff()*other.__num):
            return True
        return False
    def __ne__(self,other):
        if not self.__checkType(other):
            return None
        if (self.__Diff()*self.__num)!=(other.__Diff()*other.__num):
            return True
        return False
    def __checkType(self,other):
        if self.__type==Unit.Km or self.__type==Unit.M or self.__type==Unit.Cm:
            if other.__type==Unit.Km or other.__type==Unit.M or other.__type==Unit.Cm:
                return True
            return False
        elif self.__type==Unit.Hour or self.__type==Unit.Min or self.__type==Unit.Sec:
            if other.__type==Unit.Hour or other.__type==Unit.Min or other.__type==Unit.Sec:
                return True
            return False
        elif self.__type==Unit.Ton or self.__type==Unit.Kg or self.__type==Unit.G:
            if other.__type==Unit.Ton or other.__type==Unit.Kg or other.__type==Unit.G:
                return True
            return False
        return False
    def __Diff(self):
        if self.__type==Unit.Km:
            return 100000
        elif self.__type==Unit.M:
            return 100
        elif self.__type==Unit.Hour:
            return 3600
        elif self.__type== Unit.Min:
            return 60
        elif self.__type==Unit.Ton:
            return 1000000
        elif self.__type==Unit.Kg:
            return 1000
        else:
            return 1
    def __str__(self):
        s=str(self.__num)+"["+str(self.__type).replace("Unit.","")+"]"
        return s
    def __neg__(self):
        return PhysicalNumber(-1*self.__num,self.__type)
    def __pos__(self):
        return PhysicalNumber(self.__num,self.__type)
a=PhysicalNumber(2,Unit.Km)
b=PhysicalNumber(300,Unit.M)
print(a+b)
print(b-a)
print(-a)
print(+a)
print(a>b)
print(a<=b)
print(a==PhysicalNumber(2000, Unit.M))
a=PhysicalNumber(700, Unit.Kg)
a+=PhysicalNumber(1, Unit.Ton)
print(a)
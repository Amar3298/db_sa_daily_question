class Solution:
    def convertTemperature(self, celsius: float):
        kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        list1 = [float("%.5f"%kelvin),float("%.5f"%Fahrenheit)]
        return list1
    
obj = Solution()
res = obj.convertTemperature(36.50)
print(res)
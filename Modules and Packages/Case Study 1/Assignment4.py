# 4. Write a program to find distance between two locations when their latitude and
# longitudes are given.
# Hint: Use math module.

# d = 2R × sin⁻¹(√[sin²((θ₂ - θ₁)/2) + cosθ₁ × cosθ₂ × sin²((φ₂ - φ₁)/2)])

import math

d= 2*6.3 * math.asin(-1)(math.sqrt(math.sin((90-40)/2) + math.cos(40) * math.cos(90) * s))
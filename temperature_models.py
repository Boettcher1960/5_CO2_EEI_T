# temperature_models.py
import numpy as np

C280 = 280

def T_model71(t):
    """Quadratic temperature model from @reescatophuls.bsky"""
    return 0.000617965091650558 * t**2 - 2.45858656778789 * t + 2446.05792853123

def T_model72(t):
    """Apparent Earth System Sensitivity (AESS) model"""
    CO2 = 0.0132251 * t**2 - 51.0337 * t + 49536.7
    log2_value = np.log2(CO2 / C280)
    AESS = 8
    return AESS * log2_value

def T_model73(t):
    """Earth Climate Sensitivity (ECS) model"""
    CO2 = 0.0132251 * t**2 - 51.0337 * t + 49536.7
    log2_value = np.log2(CO2 / C280)
    ECS = 4.5
    return ECS * log2_value

def T_model76(t):
    """My best temperature model"""
    x = t - 2000
    return 0.00034 * x**2 + 0.0238 * x + 0.74

def co3_ppm(t):
    """Glen CO2 model"""
    return 0.0132251 * t**2 - 51.0337 * t + 49536.7
# temperature_models.py
# version 5b1
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


# 7 part 1
# red71_text="red @reescatophuls.bsky :  Temperature = 0.000618t² - 2.459 t + 2446.0579"
red71_text="red quadratic Temperature = 0.000618t² - 2.459 t + 2446.0579 in °C  71"
# 7.1 plot71_temperature @reescatophuls.bsky.social
# https://parisagreementtemperatureindex.com/gwfs-2-quadratic/
# (0.000617965091650558 * date*date) – (2.45858656778789*date) + 2446.05792853123
def T_model71(t):
   return 0.000617965091650558 * t**2 - 2.45858656778789 * t + 2446.05792853123
# 7.1.2 years scale x axis
years71 = np.arange(x_anf, x_end + 1 )
T_71values = T_model71(years71)
# 7.1.3. Create DataFrame for convenience
df7 = pd.DataFrame({
      "Year71": years71,
      "Modeled71": T_71values })


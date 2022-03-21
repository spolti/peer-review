from prediction import predict

# Sample data for No sepsis
data1 = {
    "HR":103,
    "O2Sat":90,
    "Temp": None,
    "SBP": None,
    "MAP": None,
    "DBP": None,
    "Resp":30,
    "EtCO2": None,
    "BaseExcess":21,
    "HCO3":45,
    "FiO2": None,
    "pH":7.37,
    "PaCO2":90,
    "SaO2":91,
    "AST":16,
    "BUN":14,
    "Alkalinephos":98,
    "Calcium":9.3,
    "Chloride":85,
    "Creatinine":0.7,
    "Glucose":193,
    "Lactate": None,
    "Magnesium":2,
    "Phosphate":3.3,
    "Potassium":3.8,
    "Bilirubin_total":0.3,
    "Hct":37.2,
    "Hgb":12.5,
    "PTT": None,
    "WBC":5.7,
    "Fibrinogen": None,
    "Platelets":317
}

# Sample data for sepsis detected
data2 = {
    "HR":72.0,
    "O2Sat":96.0,
    "Temp": None,
    "SBP":103.0,
    "MAP":62.0,
    "DBP":45.0,
    "Resp":20.0,
    "EtCO2": None,
    "BaseExcess":-1.0,
    "HCO3": None,
    "FiO2": None,
    "pH":7.4,
    "PaCO2":36.0,
    "SaO2":98.0,
    "AST": None,
    "BUN": None,
    "Alkalinephos": None,
    "Calcium": None,
    "Chloride": None,
    "Creatinine": None,
    "Glucose": None,
    "Lactate": None,
    "Magnesium": None,
    "Phosphate": None,
    "Potassium": None,
    "Bilirubin_total": None,
    "Hct": None,
    "Hgb": None,
    "PTT": None,
    "WBC": None,
    "Fibrinogen": None,
    "Platelets": None
}

predict(data1)
predict(data2)

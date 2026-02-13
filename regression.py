import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Dataset
x_multi = np.array([
    [55,70,1.0],
    [60,80,1.2],
    [65,95,1.5],
    [70,110,1.8],
    [75,125,2.0],
    [80,140,2.2],
    [85,155,2.5]
])

y = np.array([0.8,1.1,1.5,2.0,2.4,2.8,3.3])

# -----------------------------
# Train Models
# -----------------------------
x_simple = x_multi[:,0].reshape(-1,1)

model1 = LinearRegression().fit(x_simple, y)
model2 = LinearRegression().fit(x_multi, y)

poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x_simple)
model3 = LinearRegression().fit(x_poly, y)

# -----------------------------
# Model Evaluation
# -----------------------------
def evaluate(actual, predicted):
    r2 = r2_score(actual, predicted)
    mae = mean_absolute_error(actual, predicted)
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    return r2, mae, rmse

r2_s, mae_s, rmse_s = evaluate(y, model1.predict(x_simple))
r2_m, mae_m, rmse_m = evaluate(y, model2.predict(x_multi))
r2_p, mae_p, rmse_p = evaluate(y, model3.predict(x_poly))

# -----------------------------
# User Input (Safe Input)
# -----------------------------
try:
    weight = float(input("Enter Body Weight: ").strip())
    protein = float(input("Enter Protein Intake: ").strip())
    workout = float(input("Enter Workout Duration: ").strip())
except:
    print("Invalid input")
    exit()

# -----------------------------
# Predictions
# -----------------------------
pred_simple = model1.predict([[weight]])
pred_multi = model2.predict([[weight, protein, workout]])
pred_poly = model3.predict(poly.transform([[weight]]))

# -----------------------------
# Output
# -----------------------------
print("\nPredicted Muscle Gain")
print("Simple Linear Regression:", round(pred_simple[0],2), "kg")
print("Multiple Linear Regression:", round(pred_multi[0],2), "kg")
print("Polynomial Regression:", round(pred_poly[0],2), "kg")

print("\nSimple Linear Regression")
print("R²:", round(r2_s,4), " MAE:", round(mae_s,4), " RMSE:", round(rmse_s,4))

print("\nMultiple Linear Regression")
print("R²:", round(r2_m,4), " MAE:", round(mae_m,4), " RMSE:", round(rmse_m,4))

print("\nPolynomial Regression")
print("R²:", round(r2_p,4), " MAE:", round(mae_p,4), " RMSE:", round(rmse_p,4))
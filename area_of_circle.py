def area_of_circle(area):
  return 3.14 * radius * radius
if __name__=="__main__":
  try:
    radius=float(input("enter radius:"))
    print("Area:", area_of_circle(radius))
  except EOFError:
    print("Area:", area_of_circle(3))
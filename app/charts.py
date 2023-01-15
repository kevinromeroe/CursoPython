import matplotlib.pyplot as plt

def gec_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f".images/{name}.png")
  plt.close()

def pie_chart(labels,values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis("equal")
  plt.savefig("pie.png")
  plt.close()

if __name__ == "__main__":
  labels = ["a","b","c"]
  values = ["200","600","740"]
  #gec_chart(labels,values)
  pie_chart(labels, values) 
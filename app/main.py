import utils
import read_csv
import charts

#keys, values = utils.get_population()
#print(keys,values)
def run():  
  data = read_csv.read_csv("data.csv")
  country = input("ingrese pais -> ")

  result = utils.population_by_country(data,country)
  
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.gec_chart(country, labels,values)
    

if __name__ =="__main__":
  run()
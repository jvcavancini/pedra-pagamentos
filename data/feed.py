#script to feed the api with all csv data from this folder
import csv, json, requests, psycopg2

DB_HOST="localhost"
DB_NAME="last-mile"
DB_USER="postgres"
DB_PASS="jvca1996"
CSV_NAME="desafio_mini.csv"

def csv2listdict(filename='data.csv'):
    with open(filename, "r") as f:
        reader = csv.DictReader(f, delimiter=';')
        a = list(reader)
    return a

def dictdate(csv_dict):
    csv_copy=dict(csv_dict)
    csv_copy["polo_uf"]=csv_dict["polo"][:2]
    csv_copy["polo_cidade"]=csv_dict["polo"][5:]
    csv_copy["data_limite"]=csv_dict["data_limite"][6:10]+"-"+csv_dict["data_limite"][3:5]+"-"+csv_dict["data_limite"][0:2]
    del csv_copy["polo"]
    #tratando datas fora do padrao
    if(len(csv_dict["data_de_atendimento"])<6):
        csv_copy["data_atendimento"]="9999-12-31 00:00:00"
    elif('/' in csv_dict["data_de_atendimento"]):
        new_datetime=''
        string_tratada=csv_dict["data_de_atendimento"]
        string_tratada=string_tratada.replace("/","")
        string_tratada=string_tratada.replace("-","")
        string_tratada=string_tratada.replace(" ","")
        if(':' in string_tratada):
            time_sbs=string_tratada[(string_tratada.find(':')-2):]
            date_sbs=string_tratada[:(string_tratada.find(':')-2)]
        else:
            date_sbs=string_tratada
            time_sbs=""
        if(len(date_sbs)==6):
            new_datetime=new_datetime+"20"
        new_datetime=new_datetime+date_sbs[4:]+'-'+date_sbs[2:4]+'-'+date_sbs[:2]+" "+time_sbs
        csv_copy["data_atendimento"]=new_datetime
    else:
        csv_copy["data_atendimento"]=csv_copy["data_de_atendimento"]
    del csv_copy["data_de_atendimento"]
    return csv_copy

def dict2json(csv_dict):
    return json.dumps(csv_dict)

def postjson(json2post,HTTP_ADDRESS='http://localhost:5000/atendimentos'):
    r=requests.post(HTTP_ADDRESS,json=json2post)



conn=psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST)
cur=conn.cursor()

data_dict=csv2listdict(CSV_NAME)

for i in data_dict:
    udata=dict(dictdate(i))
    cur.execute("INSERT INTO last_mile(id_atendimento,id_cliente,angel,polo_cidade,polo_uf,data_limite,data_atendimento) VALUES(%s,%s,%s,%s,%s,%s,%s)",(udata["id_atendimento"],udata["id_cliente"],udata["angel"],udata["polo_cidade"],udata["polo_uf"],udata["data_limite"],udata["data_atendimento"]))
conn.commit()
cur.close()
conn.close()

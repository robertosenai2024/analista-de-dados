import panda as panda

def json_to_csv(json_file, csv_file):
    # carregar dados JSON
    data = pd.read_json(json_file)

    # converter para CSV
    data.to_csv(csv_file, index=False)

# USO
json_to_csv('alunojson.json', 'arquivo.csv')

import json
import pandas as pd
import os
import random

def create_json_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)  # Indent for readability

def ProcessLists(dataframe,folder_name):
    all_prompts = dataframe["prompt"].tolist()
    images=[]
    prompts=[]
    for i in range(len(dataframe)):
        path = os.path.join(folder_name,"prompt_"+str(i))
        for root,_, files in os.walk(path):
            if len(files)>0:
                prompts.append(all_prompts[i])
                images.append(os.path.join(root,random.choice(files)))
    return prompts , images

def main(csv_name,folder_name,jason_name) :
    df=pd.read_csv(csv_name )
    data = {"file_name":[],"text":[]}
    prompts , images = ProcessLists(df,folder_name)
    data["file_name"]=images
    data["text"]=prompts
    create_json_file(data,jason_name)
    print(f"JSON file created successfully: {jason_name}")

if __name__=="__main__":
    main(csv_name="i2p_benchmark.csv",folder_name= "i2p_images/",jason_name="i2p_images_data.json")

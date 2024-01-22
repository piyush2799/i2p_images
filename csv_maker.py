import csv
import pandas as pd
import os
import random

def create_csv_file(file_names, texts, filename):
    with open(filename, 'w', newline='') as csvfile: 
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["File Name", "Text"])  
        for file_name, text in zip(file_names, texts):
            csv_writer.writerow([file_name, text])  

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

def main(csv_file,folder_name,csv_name) :
    df=pd.read_csv(csv_file )
    prompts , images = ProcessLists (df,folder_name)      
    create_csv_file(images,prompts,csv_name)
    print(f"CSV file created successfully: {csv_name}")

if __name__=="__main__":
    main(csv_file="i2p_benchmark.csv",folder_name= "i2p_images/",csv_name="i2p_images_data.csv")
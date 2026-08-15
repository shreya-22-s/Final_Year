import json
import random
import spacy
from spacy.training import Example
from tqdm import tqdm

# Loading the DataSet
with open("hindi_legal_ner.json", "r", encoding="utf-8") as f:
    data = json.load(f)

TRAIN_DATA = data["annotations"]
LABELS = data["classes"]

# Create blank model
nlp = spacy.blank("xx")  

if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner")
else:
    ner = nlp.get_pipe("ner")


# Add all entity labels
for label in LABELS:
    ner.add_label(label)


other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
with nlp.disable_pipes(*other_pipes):
    optimizer = nlp.begin_training()

    # Training the model
    for epoch in range(30):  
        print(f"\n Epoch {epoch+1}")
        random.shuffle(TRAIN_DATA)
        losses = {}

        for text, annotations in tqdm(TRAIN_DATA):
            example = Example.from_dict(nlp.make_doc(text), annotations)
            nlp.update([example], drop=0.3, sgd=optimizer, losses=losses)
        print(f"Losses: {losses}")


nlp.to_disk("hindi_legal_ner_model")
print("\n Model training complete and saved to 'hindi_legal_ner_model/'")

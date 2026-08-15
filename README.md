# Hindi Legal Named Entity Recognition (NER)

## 📌 Project Overview

This project focuses on **Named Entity Recognition (NER) for Hindi legal text** using Natural Language Processing (NLP).

The system is designed to identify and classify important entities from Hindi legal documents, such as court names, judges, lawyers, petitioners, respondents, case numbers, dates, legal provisions, places, districts, and states.

The project uses **spaCy** to train a custom Named Entity Recognition model on an annotated Hindi legal dataset.

---

## 🎯 Objectives

The main objectives of this project are:

* To process Hindi legal text using NLP techniques.
* To automatically identify important legal entities.
* To classify entities into predefined legal categories.
* To build a custom NER model specifically for Hindi legal documents.
* To make extraction of information from legal documents faster and easier.

---

## ✨ Features

* Hindi language legal text processing
* Custom Named Entity Recognition model
* Legal-domain entity classification
* Training using an annotated dataset
* Testing the trained model on new Hindi sentences
* Extraction of entities such as:

  * Court
  * Petitioner
  * Respondent
  * Judge
  * Lawyer
  * Date
  * Organization
  * Legal Provision
  * Precedent
  * Case Number
  * Witness
  * Person
  * Place
  * District
  * State
  * Age
  * Year

---

## 🛠️ Technologies Used

* **Python**
* **Natural Language Processing (NLP)**
* **spaCy**
* **JSON**
* **tqdm**

---

## 📂 Project Structure

```text
Final_Year/
│
├── hindi_legal_ner.json
│       └── Annotated Hindi legal dataset
│
├── train_model.py
│       └── Script used to train the NER model
│
├── test_model.py
│       └── Script used to test the trained model
│
├── config.cfg
│       └── spaCy configuration
│
├── meta.json
│       └── Model metadata
│
├── tokenizer/
│       └── Tokenizer files
│
├── model/
│       └── Model data
│
├── vectors/
│       └── Vector data
│
├── lookups.bin
├── key2row
├── strings.json
└── vectors.cfg
```

---

## ⚙️ How the Project Works

The project follows these main steps:

### 1. Dataset Preparation

The annotated Hindi legal dataset is stored in:

```text
hindi_legal_ner.json
```

The dataset contains Hindi legal sentences along with the character positions and entity labels of important legal entities.

### 2. Model Training

The `train_model.py` script:

1. Loads the annotated dataset.
2. Creates a blank spaCy multilingual model.
3. Adds the NER pipeline.
4. Adds the required legal entity labels.
5. Converts the annotations into spaCy training examples.
6. Trains the model for multiple epochs.
7. Saves the trained model.

The current training script uses a blank `xx` spaCy model and trains the NER component for **30 epochs**.

### 3. Model Testing

The `test_model.py` script loads the trained model and processes a new Hindi legal sentence.

Example:

```text
प्रकरण संख्या 10/2018 में न्यायाधीश अमर सिंह और अधिवक्ता सीमा गुप्ता की उपस्थिति में गवाही दर्ज की गई।
```

The model then extracts recognized entities and displays their corresponding labels.

---

## 🧠 Named Entity Categories

The dataset contains the following entity categories:

| Entity       | Description               |
| ------------ | ------------------------- |
| COURT        | Court-related entities    |
| PETITONER    | Petitioner                |
| RESPONDENT   | Respondent                |
| JUDGE        | Judge                     |
| LAWYER       | Lawyer/advocate           |
| DATE         | Dates                     |
| ORG          | Organizations             |
| PROVISION    | Legal provisions/sections |
| PRECEDENT    | Legal precedents          |
| CASE_NUMBER  | Case/FIR numbers          |
| WITNESS      | Witnesses                 |
| OTHER_PERSON | Other persons             |
| PLACE        | Places                    |
| DISTRICT     | Districts                 |
| STATE        | States                    |
| AGE          | Age information           |
| YEAR         | Years                     |

The labels above are defined in the project's dataset.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/shreya-22-s/Final_Year.git
```

Move into the project directory:

```bash
cd Final_Year
```

Install the required Python packages:

```bash
pip install spacy tqdm
```

---

## ▶️ Train the Model

Make sure the dataset file is present in the project directory:

```text
hindi_legal_ner.json
```

Then run:

```bash
python train_model.py
```

After training, the model is saved as:

```text
hindi_legal_ner_model/
```

---

## 🧪 Test the Model

After training, run:

```bash
python test_model.py
```

The script loads the trained model and identifies entities from the sample Hindi legal sentence.

---

## 📊 Example

### Input

```text
प्रकरण संख्या 10/2018 में न्यायाधीश अमर सिंह और अधिवक्ता सीमा गुप्ता की उपस्थिति में गवाही दर्ज की गई।
```

### Expected Output

The model attempts to identify entities such as:

```text
10/2018 → CASE_NUMBER
अमर सिंह → JUDGE
सीमा गुप्ता → LAWYER
```

The exact output depends on the trained model.

---

## 🔍 Applications

This project can be useful for:

* Legal document analysis
* Hindi legal information extraction
* Automatic case information extraction
* Legal document search
* Court document processing
* Legal research assistance
* Building Hindi legal NLP applications

---

## 🔮 Future Scope

Future improvements could include:

* Improving model accuracy with a larger dataset.
* Adding more legal entity categories.
* Using a Hindi-specific pretrained language model.
* Developing a web interface for users.
* Supporting PDF legal documents.
* Extracting entities from complete court judgments.
* Adding automatic legal document summarization.
* Integrating the model with a legal search system.
* Evaluating the model using Precision, Recall, and F1-score.

---

## 👩‍💻 Project

**Final Year Project**

**Domain:** Natural Language Processing (NLP) / Artificial Intelligence

**Focus:** Hindi Legal Named Entity Recognition

---

## 📄 License

This project is developed for academic and educational purposes.

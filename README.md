# Venom Molecular Function Prediction AI

## Intro

Regeneron International Science and Engineering Fair 2023 project titled: "A Novel Application of Machine Learning Algorithms on Toxin Proteins to Predict Molecular Function". Built by Ameya Kulkarni and Praneeth Muvva.

The model takes in an amino acid sequence for a protein of your choosing, and outputs the top 10 most likely Gene Ontology (GO) functional categories with their respective probabilities. GO classes are from our selected cohort of 91 of the most prevalent venom protein functional classes out of UniProt venom sequences.

GO codes can easily be identified via public databases and resources such as UniProt or QuickGO. For example, GO:0090729 corresponds to "toxin activity", GO:0030550 corresponds to "Acetylcholine receptor inhibition", etc.

## Demo

[![Demo Video](https://img.youtube.com/vi/dc1ohRymKSs/0.jpg)](https://www.youtube.com/watch?v=dc1ohRymKSs)

## How to Use

1. Clone this git repo to your computer
2. Install the dependencies listed in `requirements.txt`. You can do this with in the command line with `pip install -r requirements.txt`, recommended to do this in a virtual environment.
3. Run `app.py`, and open the app in the browser at http://127.0.0.1:5000

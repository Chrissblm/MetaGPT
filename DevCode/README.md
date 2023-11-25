
python examples/build_customized_multi_agents.py --add_human True  --code_review
code_review


# Must have conda installed
# It costs approximately $0.2 (in GPT-4 API fees) to generate one example with analysis and design, and around $2.0 for a full project.

conda create -n metagpt python=3.11.4
conda activate metagpt
npm --version # to check you have npm installed
# optional: install node if you don't have it
npm install -g @mermaid-js/mermaid-cli
git clone https://github.com/geekan/metagpt
cd metagpt
python -m pip install -r requirements.txt
python setup.py install
# create openai API key
# insert API key into config/config.yaml
# make sure to set the model correctly depending on which model you have access to
python startup.py "Write a cli snake game based on pygame" # optional --code_review True (better code, costs more)
# if you get ModuleNotFoundError: No module named 'bs4’, run "python -m pip install bs4"
python startup.py "Write a cli snake game based on pygame" # do this again if you got the ModuleNotFoundError
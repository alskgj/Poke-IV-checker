# Poke-IV-checker

A simple pokemon IV checker. Just enter your credentials
in a config file (file has to be in config/ and end with ".ini")
and this programm will change the name of all your pokemon to
n% a/d/s where (a, d, s) corresponds to your pokemons 
(attack IV, defense IV, stamina IV) respectively and n is the percentage
of the maximum values for all combined.

## Installation
- Install python3.
- Clone [this project](https://github.com/alskgj/Poke-IV-checker.git) with `git clone`
- Enter the applications folder and install the requirements of this project with `pip3 install -r requirements.txt`

## Usage
- Change the example configfile or create a new configfile.
- Run with `python3 main.py`

## Usage with Docker
If you'd like to keep your local system clean you can execute this
project in a container environment provided by Docker:

- Build the Dockerfile: 'docker build -t <myname>/pokeiv .'
- Run the script (you have to hand over the current directory in order to provide the config): 'docker run -v $(pwd):/workspace -it <myname>/pokeiv'

# Recopilación de Información

Repositorio principal del modulo de recopilacion de informacion.

## Requerimientos

Instalar go

Usar el [siguiente enlace](https://tzusec.com/how-to-install-golang-in-kali-linux/).

En el paso 5 es necesario hacer las siguientes modificaciones:

Kali utiliza zsh en lugar de bash, por lo tanto el archivo a editar es ~/.zshrc

Seguir las instrucciones, pero al insertar cosas en el archivo zshrc ponemos:

```
export GOPATH=/home/kali/go-workspace
export GOROOT=/usr/local/go
PATH=$PATH:$GOROOT/bin/:$GOPATH/bin:/home/kali/.local/bin
```


## Herramientas

Lista de herramientas para el modulo.

### Mapcidr
```
go install github.com/projectdiscovery/mapcidr/cmd/mapcidr@latest
```

### Dnsx
```
go install github.com/projectdiscovery/dnsx/cmd/dnsx@latest
```

### Murmurhash
```
git clone https://github.com/Viralmaniar/MurMurHash.git
cd MurMurHash/
pip3 install -r requirements.txt

```

### CTFR
```
git clone https://github.com/UnaPibaGeek/ctfr.git
cd ctfr
pip3 install -r requirements.txt
```

### DNSvalidator
```
git clone https://github.com/vortexau/dnsvalidator.git
cd dnsvalidator/
python3 setup.py install
```

### Massdns
```
git clone https://github.com/blechschmidt/massdns.git
cd massdns
make
sudo make install
```

### Puredns
```
go install github.com/d3mondev/puredns/v2@latest
```

### Gotator
```
git clone https://github.com/Josue87/gotator.git
cd gotator
go build
go install
```

### Analytics Relationships
```
git clone https://github.com/Josue87/AnalyticsRelationships.git
cd AnalyticsRelationships/
go build -ldflags "-s -w"
go install
```

### Cero
```
go install github.com/glebarez/cero@latest
```

### Gospider
```
go install github.com/jaeles-project/gospider@latest
```

### Unfurl
```
go install github.com/tomnomnom/unfurl@latest
```

### IP range to CIDR
```
go install github.com/raspi/ip-range-to-CIDR@latest
```

### Waybackurl
```
go install github.com/tomnomnom/waybackurls@latest
```

### Github-Search
```
git clone https://github.com/gwen001/github-search
cd github-search
pip3 install -r requirements2.txt

```

### Amass
```
sudo apt update
sudo apt install amass
```

### Cloud Enum
```
git clone https://github.com/initstring/cloud_enum
cd cloud_enum
pip3 install -r requirements.txt
```

### Sublist3r

```
git clone https://github.com/aboul3la/Sublist3r.git .
cd Sublist3r
pip3 install -r requirements.txt
```

### Spiderfoot
```
wget https://github.com/smicallef/spiderfoot/archive/v3.5.tar.gz
tar zxvf v3.5.tar.gz
cd spiderfoot-3.5
pip3 install -r requirements.txt
```

### Httpx
```
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
```

### Eyewitness
```
git clone https://github.com/FortyNorthSecurity/EyeWitness
cd EyeWitness/Python/setup
sudo ./setup.sh
```

### Aquatone
```
mkdir aquatone
```

Get release [from here](https://github.com/michenriksen/aquatone/releases/).

```
unzip <file>

Necesitamos el binario de chrome para que funcione

git clone https://github.com/scheib/chromium-latest-linux
cd chromium-latest-linux
./update.sh

El binario que necesitamos esta en /chromium-latest-linux/latest/chrome
```

### Gobuster
```
go install github.com/OJ/gobuster/v3@latest
```

### Wappalyzer
```
git clone https://github.com/AliasIO/wappalyzer.git
cd wappalyzer
yarn install
yarn run link
```

### Nuclei
```
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
```

### Spoofcheck
```
git clone https://github.com/a6avind/spoofcheck
cd spoofcheck
pip3 install -r requirements.txt
```

### Subzy
```
go install -v github.com/lukasikic/subzy@latest
```

### Exiftool
```
sudo apt install libimage-exiftool-perl
```


### Infoga
```
git clone https://github.com/m4ll0k/Infoga.git
cd Infoga
sudo python setup.py install
```

### Sherlock
```
docker build -t mysherlock-image .
docker run --rm -t mysherlock-image user123
```

### Facebook-scraper
```
pip3 install facebook-scraper
```

### Instagram-scraper
```
pip3 install instagram-scraper
```

### OSRFramework
```
git clone https://github.com/i3visio/osrframework
cd osrframework
pip3 install -r requirements.txt
pip3 install .
```

### LinkedInt

```
git clone https://github.com/vysecurity/LinkedInt
cd LinkedInt
```

Editar el archivo requirements.txt. Quitar la linea "urllib3==1.26.5".

```
pip3 install -r requirements.txt
```


### OnionSearch
```
git clone https://github.com/megadose/OnionSearch.git
cd OnionSearch
sudo python3 setup.py install
```






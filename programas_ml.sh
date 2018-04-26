echo "============= Dependencias e programas MAC e Linux ============= "

echo "--> Step 1....."
mkdir homebrew && curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C homebrew

echo "--> Step 2....."
curl http://bootstrap.pypa.io/get-pip.py -o get-pip.py

echo "--> Step 3....."
pip install virtualenv
echo "Instrução: cd my_app --> virtualenv venv --> source venv/bin/activate"

echo "--> Step 4...."
brew install heroku/brew/heroku

echo "--> Step 5....."
brew install npm

echo "--> Step 6....."
echo "Mac[1] ou Linux[2]?"
read op

if [ $op == 1 ];
  then
	git clone https://github.com/Eduardojvr/Personalizacao_Bash_MacBook.git
	cd Personalizacao_Bash_MacBook
	cp .bash_profile  ../
	cd
	rm -rf Personalizacao_Bash_MacBook
  else
	cd
	git clone https://github.com/Eduardojvr/Scripts.git
	cd Scripts
	cp bashrc  ../
	cd 
	rm -rf .bashrc
	cp bashrc .bashrc
	cd
	rm -rf Scripts && rm -rf bashrc
fi
cd

echo "--> Fim"

echo "Qual site deseja acessar?"
read site
echo "Abrindo $site ......"
lynx $site -use_mouse -accept_all_cookies 


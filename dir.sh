cat ~/dir.txt 
#git show --stat

#git rm -r --cached .
#git diff --name-only
#git show --name-only 
#git show --name-only  | awk -F "/*[^/]*/*$" '{ print ($1 == "" ? "." : $1); }' | sort | uniq  > ~/dir.txt 
git show --stat  | awk -F "/*[^/]*/*$" '{ print ($1 == "" ? "." : $1); }' | sort | uniq  > ~/dir.txt 
#git diff --name-only  | awk -F "/*[^/]*/*$" '{ print ($1 == "" ? "." : $1); }' | sort | uniq  > ~/dir.txt 
cat ~/dir.txt 
#while IFS= read -r line; do

#      if [ $line = . ]
#      then 
#        echo "ignore"
#      else 
#        cd $line
#        sh script.sh
#        cd ..
#      fi
#  done  < ~/dir.txt

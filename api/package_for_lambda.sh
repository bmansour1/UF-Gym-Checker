set -eux pipefail
pip install -t lib -r requirements.txt
(cd lib; zip ../lambda_function.zip -r .)
zip lambda_function_api.zip -u backend.py

rm -rf lib
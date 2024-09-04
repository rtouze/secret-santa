sync:
	uv pip compile requirements.in -o requirements.txt
	uv pip compile dev-requirements.in -o dev-requirements.txt
	uv pip sync requirements.txt dev-requirements.txt

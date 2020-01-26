deploy-alexa-skill:
	cd alexa-skill && \
	yarn deploy:dev

build-alexa-skill:
	cd alexa-skill && \
	yarn alexa:build

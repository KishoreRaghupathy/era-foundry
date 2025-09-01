# Runtime image layering on base
FROM era-foundry-base:0.1

WORKDIR /workspace
COPY . /workspace

CMD ["bash"]

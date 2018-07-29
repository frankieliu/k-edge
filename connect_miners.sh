
# this sets up the discovery of miner nodes in the blockchain network

#curl -d '{"nodes": "http://127.0.0.1:5001,http://127.0.0.1:5002"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/nodes/register
#curl -d '{"nodes": "http://127.0.0.1:5000,http://127.0.0.1:5002"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5001/nodes/register
#curl -d '{"nodes": "http://127.0.0.1:5000,http://127.0.0.1:5001"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5002/nodes/register

curl -F 'nodes="http://127.0.0.1:5001,http://127.0.0.1:5002"' -X POST http://127.0.0.1:5000/nodes/register
curl -F 'nodes="http://127.0.0.1:5000,http://127.0.0.1:5002"' -X POST http://127.0.0.1:5001/nodes/register
curl -F 'nodes="http://127.0.0.1:5000,http://127.0.0.1:5001"' -X POST http://127.0.0.1:5002/nodes/register

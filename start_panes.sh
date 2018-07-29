tmux send-keys -t ":1.0" 'python blockchain.py' C-m
sleep 0.4
tmux send-keys -t ":1.1" 'python blockchain.py' C-m
sleep 0.4
tmux send-keys -t ":1.2" 'python blockchain.py' C-m
tmux send-keys -t ":1.3" 'python blockchain_client.py' C-m

kedge=$(pwd)
tmux send-keys -t ":1.0" "cd ${kedge}/blockchain; python blockchain.py" C-m
sleep 0.4
tmux send-keys -t ":1.1" "cd ${kedge}/blockchain; python blockchain.py" C-m
sleep 0.4
tmux send-keys -t ":1.2" "cd ${kedge}/blockchain; python blockchain.py" C-m
tmux send-keys -t ":1.3" "cd ${kedge}/blockchain-client; python blockchain_client.py" C-m

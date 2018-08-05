# tmux set -g base-index 0
tmux if-shell 'tmux select-window -t :0' '' 'new-window -t :0'
tmux if-shell 'tmux select-window -t :1' '' 'new-window -t :1'

tmux select-window :1
tmux kill-window
tmux new-window -t :1

tmux split-window -v -t :1.0
tmux split-window -h -t :1.0
tmux split-window -h -t :1.2
tmux split-window -v -t :1.3

# tmux split-window -h -t :1.0
# tmux split-window -h -t :1.1
# tmux split-window -h -t :1.2
# tmux split-window -h -t :1.3



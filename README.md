
# This is a fork of adilmoujahid's wonderful blockchain demo
# k-edge
  - decentralized edge efficient mining
  - additions were made to test out a different consensus algorithm
# Dependencies
  - tmux
# Running
  - start a tmux session: $ tmux
  - create a set of panels in tmux (use create_panes.sh)
  
  | a | b|
| d | c|

    | 0 | 1  |
    |   |    |
    |---|----|
    | 2 | 3  |
    |   | -- |
    |   | 4  |

  - cd k-edge
  - ./stop_panes.sh
  - 0: cd to blockchain
  - 1: cd to blockchain
  - 2: cd to blockchain
  - 3: cd to blockchain-client
  - 4: cd to k-edge
  - ./start_panes.sh
  - ./connect_miners.sh
  - ./start_browser.sh
  - in browser
    - go to client
    - generate wallet
    - make a transaction (reload for defaults)
    - go to miners
    - refresh each one of them to see the transaction
    - for each miner, click on mine
  - in cli, ./resolve.sh
  - in browser
    - for each miner, see the resolution
  - in cli, see the proof-of-work and show the metering

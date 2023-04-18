```mermaid
sequenceDiagram
  participant main
  participant welcome
  participant sweet
  participant salty
  participant redo
  main->>welcome
  welcome->>sweet
  welcome->>salty
  welcome->>welcome
  sweet->>redo
  salty->>redo
```

# two-projects-one-repo

> ⚠️ **WARNING: The following repository contains content of an extremely technical nature. Viewer discretion is advised. Not suitable for those with dependency anxiety, npm phobia, or a functioning sense of proportionality.**

---

You've heard the legends. You've seen the look on people's faces. Now witness for yourself what happens when **two projects share one repository** -- and both of them use enterprise-grade tooling to count to **2**.

---

## What Is This

This repository contains **two projects**. We know this because we counted. Twice. Using different languages. With unnecessary dependencies.

| Project | Language   | Purpose                | Dependencies Required                                                                                     |
|---------|------------|------------------------|-----------------------------------------------------------------------------------------------------------|
| `/python` | Python     | Count directories      | numpy, pandas, scipy, matplotlib, requests, Pillow, scikit-learn, tensorflow                              |
| `/npm`    | JavaScript | Also count directories | express, react, webpack, babel, typescript, mongoose, redis, graphql, puppeteer, ffmpeg, mathjs, and more |

The answer is `2`.

It was always going to be `2`.

---

## Running the Python Project

```bash
cd python
pip install -r requirements.txt  # ~4GB, give it a minute
python count_projects.py
```

**Output:**

```
Number of projects: 2
```

TensorFlow was loaded. It did not help.

---

## Running the npm Project

```bash
cd npm
npm install  # This will take a while. Maybe get lunch.
node count_projects.js
```

**Output:**

```
Number of projects: 2
```

Puppeteer downloaded a full copy of Chromium. For a directory listing.

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                      two-projects-one-repo                      │
│                                                                 │
│   ┌─────────────────────┐     ┌─────────────────────────────┐   │
│   │       /python       │     │            /npm             │   │
│   │                     │     │                             │   │
│   │  tensorflow         │     │  react                      │   │
│   │  scikit-learn    ───┼──┐  │  webpack                 ───┼──┐│
│   │  pandas             │  │  │  graphql                    │  ││
│   │  scipy              │  │  │  puppeteer                  │  ││
│   │  matplotlib         │  │  │  ffmpeg                     │  ││
│   │  numpy              │  │  │  mongoose                   │  ││
│   │                     │  │  │  mathjs                  ───┼──┤│
│   │  os.listdir()   <───┼──┘  │                             │  ││
│   └─────────────────────┘     │  fs.readdirSync()       <───┼──┘│
│            │                  └─────────────────────────────┘   │
│            │                               │                    │
│            └──────────────┬────────────────┘                    │
│                           ▼                                     │
│                           2                                     │
└─────────────────────────────────────────────────────────────────┘
```

---

## FAQ

**Q: Why does the Python version import TensorFlow to count directories?**  
A: Deep learning.

**Q: Why does the npm version install React to read the filesystem?**  
A: We may want to render the result as a component later.

**Q: What does mathjs add here that JavaScript's** `+` **operator doesn't?**  
A: Confidence.

**Q: Does Puppeteer actually do anything?**  
A: It downloaded Chromium. That's something.

**Q: Could you have done this with two lines of shell script?**  
A: Please leave.

---

## Requirements

- Python 3.8+ and approximately one free afternoon
- Node.js 18+ and the emotional fortitude to watch `node_modules` grow
- Disk space (please have disk space)
- No strong opinions about dependency hygiene

---

## Contributing

If you would like to add a third project that also counts to 2, please open a pull request. Bonus points if it requires a Docker container.

---

## License

MIT. Take it. Use it. Count things.

---

*"I have seen things you people wouldn't believe. A TensorFlow import for a directory listing. Chromium downloaded to count to two. All those dependencies, lost in time, like tears in rain."*
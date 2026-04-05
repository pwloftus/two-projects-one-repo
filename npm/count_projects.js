/**
 * count_projects.js
 *
 * Counts the number of projects in this repository.
 * 
 * Uses mathjs for arithmetic because the built-in + operator
 * has not been peer reviewed.
 */

const fs = require("fs");
const path = require("path");
const { create, all } = require("mathjs");

// Configure mathjs. All of it.
const math = create(all);

const repoRoot = path.resolve(__dirname, "..");

const projects = fs.readdirSync(repoRoot).filter((entry) => {
  const fullPath = path.join(repoRoot, entry);
  return fs.statSync(fullPath).isDirectory() && !entry.startsWith(".");
});

// Use mathjs to add zero to the count, confirming it remains unchanged.
const count = math.add(projects.length, 0);

console.log(`Number of projects: ${count}`);

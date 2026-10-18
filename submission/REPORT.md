# CrewAI Build Report

**Name:** Sai Rahul Panthangi
**Topic I used:** Quantum Computing

## 1. What I changed
I modified the backstory of the Writer agent in `main.py` to turn it into a harsh, highly skeptical senior technical reviewer who demands rigorous benchmarks and challenges hype. I chose this change because it directly alters the tone and depth of the generated explainer without breaking the structure of the tasks or crew definition, making it easy to observe a distinct behavioral shift in the final output.

## 2. How CrewAI works
CrewAI orchestrates multi-agent workflows using three core abstractions: agents, tasks, and crews. Agents are individual worker definitions equipped with a role, goal, backstory, and underlying LLM configuration. Tasks define specific objectives, expected outputs, and are assigned to particular agents. The crew ties them together, managing the execution flow—either sequentially or hierarchically—passing context and outputs from one task to the next. My change worked because modifying the Writer's backstory shifted its prompt-level persona, causing it to evaluate and rewrite the researcher's findings through a much more critical, rigorous lens.

## 3. Evidence
In the first run (saved in `run1_original.txt` and `explainer_run1.md`), the writer produced a standard, enthusiastic educational overview. In the second run (`run2_changed.txt` and `explainer_run2.md`), the output adopted a sharp, critical tone, explicitly questioning hardware limitations and error correction bottlenecks. One minor hurdle was ensuring the topic string was handled properly in PowerShell quotes; verifying the terminal logs solved it immediately.

## 4. Choosing a framework
CrewAI is ideal for projects that rely heavily on role-playing personas, sequential task delegation, and quick prototyping of team-based text generation. Compared to LangGraph, which requires manual graph routing and node-by-node state management, CrewAI abstracts much of the boilerplate away, making it much faster to spin up a collaborative agent pipeline. However, if a project required complex, cyclic state loops with conditional branching, LangGraph would provide necessary granular control that CrewAI abstracts away.

## 5. Verification and AI use
I verified the output by reading through both generated explainer files to ensure the tone shifted as expected and that technical facts remained grounded. No external web access was used by the kit, so facts rely on model memory. AI assistance was used solely to draft and format this report template.

from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill


def main():
    candidates_list = load_candidates_from_json("candidates.json")

    app = Flask(__name__)

    @app.route("/")
    def page_index():
        return render_template('list.html', candidates=candidates_list)

    @app.route("/candidate/<int:pk>")
    def page_id(pk):
        candidate = get_candidate(candidates_list, pk)
        return render_template('single.html', candidate=candidate)

    @app.route("/search/<candidate_name>")
    def page_search(candidate_name):
        candidates = get_candidates_by_name(candidates_list, candidate_name)
        return render_template('search.html', candidates=candidates, candidates_count=len(candidates))

    @app.route("/skill/<skill_name>")
    def page_skill(skill_name):
        candidates = get_candidates_by_skill(candidates_list, skill_name)
        return render_template('skill.html', candidates=candidates, candidates_count=len(candidates), skill=skill_name)

    app.run(host='127.0.0.1', port=80)

    app.run()


if __name__ == '__main__':
    main()

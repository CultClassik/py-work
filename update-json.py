import json, sys

new_json = json.loads(sys.argv[1])
all_tags = json.loads(open('test.json', 'r').read())

for key in new_json["tags"].keys():
    diffs = set(new_json["tags"][key]) - set(all_tags["tags"][key])
    all_tags["tags"][key] = all_tags["tags"][key] + list(diffs)
    all_tags["tags"][key].sort()

new_content = {
    "tags": sorted(all_tags["tags"])
}
print(new_content)

# to run:
# python update-json.py '{"tags":{"app":["app01","app03"],"env":["dr","test"]}}'
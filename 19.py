import re
import functools
import multiprocessing

def do_blueprint(blueprint, max_rounds):
    bp_num, ore_cost_ore, ore_cost_clay, ore_cost_obs, clay_cost_obs, ore_cost_geo, obs_cost_geo = map(int,blueprint)
    max_ore_cost = max(ore_cost_ore, ore_cost_clay, ore_cost_obs, ore_cost_geo)
    max_clay_cost = clay_cost_obs
    max_obs_cost = obs_cost_geo
    @functools.cache
    def round(round_num, ore, clay, obsidian, geodes, ore_robots, clay_robots, obsidian_robots, geode_robots):
        max_ore_can_be_spent = (max_rounds-1-round_num)*max_ore_cost
        max_clay_can_be_spent = (max_rounds-1-round_num)*max_clay_cost
        max_obs_can_be_spent = (max_rounds-1-round_num)*max_obs_cost
        if round_num >= max_rounds:
            return geodes
        possible_args = []

        if obsidian >= obs_cost_geo and ore >= ore_cost_geo:
            possible_args.append((round_num+1,
                                    min(max_ore_can_be_spent, ore+ore_robots-ore_cost_geo),
                                    min(max_clay_can_be_spent, clay+clay_robots),
                                    min(max_obs_can_be_spent, obsidian+obsidian_robots-obs_cost_geo),
                                    geodes+geode_robots,
                                    ore_robots,
                                    clay_robots,
                                    obsidian_robots,
                                    geode_robots+1))
        if obsidian_robots < max_obs_cost and clay >= clay_cost_obs and ore >= ore_cost_obs:
            possible_args.append((round_num+1,
                                    min(max_ore_can_be_spent, ore+ore_robots-ore_cost_obs),
                                    min(max_clay_can_be_spent, clay+clay_robots-clay_cost_obs),
                                    min(max_obs_can_be_spent, obsidian+obsidian_robots),
                                    geodes+geode_robots,
                                    ore_robots,
                                    clay_robots,
                                    obsidian_robots+1,
                                    geode_robots))
        if clay_robots < max_clay_cost and ore >= ore_cost_clay:
            possible_args.append((round_num+1,
                                    min(max_ore_can_be_spent, ore+ore_robots-ore_cost_clay),
                                    min(max_clay_can_be_spent, clay+clay_robots),
                                    min(max_obs_can_be_spent, obsidian+obsidian_robots),
                                    geodes+geode_robots,
                                    ore_robots,
                                    clay_robots+1,
                                    obsidian_robots,
                                    geode_robots))
        if ore_robots < max_ore_cost and ore >= ore_cost_ore:
            possible_args.append((round_num+1,
                                    min(max_ore_can_be_spent, ore+ore_robots-ore_cost_ore),
                                    min(max_clay_can_be_spent, clay+clay_robots),
                                    min(max_obs_can_be_spent, obsidian+obsidian_robots),
                                    geodes+geode_robots,
                                    ore_robots+1,
                                    clay_robots,
                                    obsidian_robots,
                                    geode_robots))
        possible_args.append((round_num+1,
                                    min(max_ore_can_be_spent, ore+ore_robots),
                                    min(max_clay_can_be_spent, clay+clay_robots),
                                    min(max_obs_can_be_spent, obsidian+obsidian_robots),
                                    geodes+geode_robots,
                                    ore_robots,
                                    clay_robots,
                                    obsidian_robots,
                                    geode_robots))
        return max(round(*args) for args in possible_args)
    return ((bp_num, round(0,0,0,0,0,1,0,0,0)))

def bp24(blueprint):
    return do_blueprint(blueprint,24)

def bp32(blueprint):
    return do_blueprint(blueprint,32)

def main():
    regex = re.compile(r".* (\d+):.* (\d+) .* (\d+) .* (\d+) .* (\d+) .* (\d+) .* (\d+) .*")

    blueprints = []
    lines = open("19.dat").read().splitlines()
    for line in lines:
        m = regex.match(line)
        blueprints.append(m.groups())

    pool_obj = multiprocessing.Pool()
    results = pool_obj.map(bp24, blueprints)
    s = 0
    for i,j in results:
        s += i*j
    print(s)

    pool_obj2 = multiprocessing.Pool()
    results2 = pool_obj2.map(bp32, blueprints[:3])
    print(results2)
    p = 1
    for i,j in results2:
        p *= j
    print(p)

if __name__ == "__main__":
    main()
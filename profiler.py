import cProfile
import pstats
import slideReader
#aight so base of most recent profile on a big one, reading the slides in takes 80% of the time
#took  172 seconds
#changes to grab() frames that arnet needed
#took 89 seconds

profile = cProfile.Profile()
profile.run('slideReader.main()')
ps = pstats.Stats(profile)
ps.strip_dirs().sort_stats(pstats.SortKey.CUMULATIVE)
ps.print_stats()
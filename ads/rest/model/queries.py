from flask_restplus import reqparse, inputs
from ads import settings


job_query = reqparse.RequestParser()
job_query.add_argument('q', required=True,
                        location='args',
                        help="Must provide an occupation name!")
job_query.add_argument(settings.LIMIT,
                           type=inputs.int_range(0, settings.MAX_LIMIT),
                           default=10)
job_query.add_argument(settings.OFFSET, default=0)


allJobs_query = reqparse.RequestParser()
allJobs_query.add_argument('q')
allJobs_query.add_argument(settings.OFFSET,
                           type=inputs.int_range(0, settings.MAX_OFFSET),
                           default=0)
allJobs_query.add_argument(settings.LIMIT,
                            type=inputs.int_range(0, settings.MAX_LIMIT),
                            default=10)
allJobs_query.add_argument(settings.SHOW_EXPIRED, choices=['true', 'false'], default='false')
allJobs_query.add_argument(settings.PLACE, action='append')


skillsandtraits_query = reqparse.RequestParser()
skillsandtraits_query.add_argument('q', required=True,
                                   location='args',
                                   help="Must provide an occupation name!")
skillsandtraits_query.add_argument(settings.LIMIT,
                                   type=inputs.int_range(0, settings.MAX_LIMIT))
skillsandtraits_query.add_argument(settings.PLACE, action='append')

# heat map api's queries
heatmap_query = reqparse.RequestParser()
heatmap_query.add_argument('q', required=True,
                           location='args', help='Must provide an occupation name')
heatmap_query.add_argument(settings.LIMIT,
                           type=inputs.int_range(0, settings.MAX_LIMIT),
                           default=10)
heatmap_query.add_argument(settings.OFFSET, default=0)


# job count api's queries
jobcount_query = reqparse.RequestParser()
jobcount_query.add_argument('q', required=True,
                           location='args', help='Must provide an occupation name')
jobcount_query.add_argument(settings.LIMIT,
                           type=inputs.int_range(0, settings.MAX_LIMIT),
                           default=10)
jobcount_query.add_argument(settings.OFFSET, default=0)
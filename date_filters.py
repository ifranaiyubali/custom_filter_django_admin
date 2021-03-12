from django.contrib.admin import ModelAdmin, SimpleListFilter


class ByYearFilter(SimpleListFilter):
    title = 'Year'  # a label for our filter
    parameter_name = 'ByYear'  # parameter that will used in url query

    def lookups(self, request, model_admin):
      '''lookups , looks up a field in in the modle the filter is applied to
         model_admin provides the model that filter will be applied to
         so from model I am looking up field year then then returning a tuple for it 
         this is to display the filter tuple[1] and use in query tuple[0]'''
        years = set([c.year for c in model_admin.model.objects.all()])
        return sorted([(c.year, c.year) for c in years])

    def queryset(self, request, queryset):
        ''' queryset definition has a parameter queryset which query the model in question
        then we can addtionaly apply more filter to suit mimck the filter we display
        so  to the querset apply a filter to date field year for year only and lookup self.value() which is tuple[0]
        value from lookup'''
        if self.value():
            return queryset.filter(year__year=self.value())


class ByMonthFilter(SimpleListFilter):
    title = 'Year'  # a label for our filter
    parameter_name = 'ByYear'  # you can put anything here

    def lookups(self, request, model_admin):
        '''lookups , looks up a field in in the model the filter is applied to
         model_admin provides the model that filter will be applied to
         so from model I am looking up field year_month then then returning a tuple for it 
         this is to display the filter tuple[1] and use in query tuple[0]
         I am using set because year_month field has Month and Year and there are multiple same year values 
         so set removes duplicate year value, do not get confused by filter class name, this filter just shows up as year'''
        years = set([c.year_month for c in model_admin.model.objects.all()])
        return sorted(list(set([(c.year, c.year) for c in years])))

    def queryset(self, request, queryset):
        ''' queryset definition has a parameter queryset which query the model in question
        then we can addtionaly apply more filter to suit mimck the filter we display
        so  to the querset apply a filter to date field year_month for year only and lookup self.value() which is tuple[0]
        value from lookup'''
        if self.value():
            return queryset.filter(year_month__year=self.value())
